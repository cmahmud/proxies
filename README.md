# SyndProxy private pool

## Current pool

- Alive now: 755
- Gold now: 396
- HTTP: 200 alive / 90 gold
- HTTPS: 143 alive / 26 gold
- SOCKS4: 175 alive / 129 gold
- SOCKS5: 237 alive / 151 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31919
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
