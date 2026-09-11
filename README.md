# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 458
- HTTP: 121 alive / 84 gold
- HTTPS: 57 alive / 33 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 197 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49228
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
