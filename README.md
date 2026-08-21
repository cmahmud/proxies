# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 420
- HTTP: 245 alive / 93 gold
- HTTPS: 137 alive / 27 gold
- SOCKS4: 211 alive / 138 gold
- SOCKS5: 250 alive / 162 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29411
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
