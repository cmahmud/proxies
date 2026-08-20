# SyndProxy private pool

## Current pool

- Alive now: 1536
- Gold now: 625
- HTTP: 586 alive / 208 gold
- HTTPS: 494 alive / 114 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 235 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24029
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
