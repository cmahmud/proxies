# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 599
- HTTP: 450 alive / 183 gold
- HTTPS: 283 alive / 113 gold
- SOCKS4: 235 alive / 147 gold
- SOCKS5: 227 alive / 156 gold

## Historical pool

- Discovered: 124855
- Ever alive: 19456
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
