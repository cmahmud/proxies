# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 393
- HTTP: 293 alive / 80 gold
- HTTPS: 154 alive / 19 gold
- SOCKS4: 237 alive / 149 gold
- SOCKS5: 235 alive / 145 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29631
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
