# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 442
- HTTP: 132 alive / 78 gold
- HTTPS: 111 alive / 25 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47649
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
