# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 444
- HTTP: 135 alive / 79 gold
- HTTPS: 104 alive / 26 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47649
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
