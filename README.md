# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 372
- HTTP: 193 alive / 77 gold
- HTTPS: 151 alive / 16 gold
- SOCKS4: 183 alive / 119 gold
- SOCKS5: 223 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26124
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
