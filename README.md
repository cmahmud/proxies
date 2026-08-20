# SyndProxy private pool

## Current pool

- Alive now: 1789
- Gold now: 685
- HTTP: 684 alive / 236 gold
- HTTPS: 565 alive / 143 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 322 alive / 163 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24487
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
