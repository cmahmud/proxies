# SyndProxy private pool

## Current pool

- Alive now: 1628
- Gold now: 630
- HTTP: 568 alive / 212 gold
- HTTPS: 463 alive / 117 gold
- SOCKS4: 236 alive / 146 gold
- SOCKS5: 361 alive / 155 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24084
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
