# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 453
- HTTP: 134 alive / 84 gold
- HTTPS: 136 alive / 38 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44747
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
