# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 392
- HTTP: 247 alive / 85 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 193 alive / 137 gold
- SOCKS5: 237 alive / 151 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29757
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
