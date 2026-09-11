# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 440
- HTTP: 108 alive / 78 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49171
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
