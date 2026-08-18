# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 360
- HTTP: 344 alive / 54 gold
- HTTPS: 205 alive / 13 gold
- SOCKS4: 225 alive / 142 gold
- SOCKS5: 237 alive / 151 gold

## Historical pool

- Discovered: 107115
- Ever alive: 14871
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
