# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 525
- HTTP: 389 alive / 155 gold
- HTTPS: 256 alive / 91 gold
- SOCKS4: 205 alive / 137 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19892
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
