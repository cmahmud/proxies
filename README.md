# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 370
- HTTP: 260 alive / 91 gold
- HTTPS: 196 alive / 15 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 212 alive / 123 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18278
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
