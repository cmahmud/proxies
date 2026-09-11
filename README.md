# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 443
- HTTP: 106 alive / 84 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49206
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
