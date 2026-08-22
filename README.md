# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 400
- HTTP: 205 alive / 91 gold
- HTTPS: 146 alive / 32 gold
- SOCKS4: 182 alive / 125 gold
- SOCKS5: 238 alive / 152 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31921
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
