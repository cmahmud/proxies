# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 416
- HTTP: 227 alive / 84 gold
- HTTPS: 164 alive / 22 gold
- SOCKS4: 212 alive / 156 gold
- SOCKS5: 221 alive / 154 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27487
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
