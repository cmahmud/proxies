# SyndProxy private pool

## Current pool

- Alive now: 1726
- Gold now: 686
- HTTP: 655 alive / 237 gold
- HTTPS: 536 alive / 143 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 321 alive / 163 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24497
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
