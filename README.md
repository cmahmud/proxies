# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 443
- HTTP: 122 alive / 79 gold
- HTTPS: 121 alive / 29 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47639
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
