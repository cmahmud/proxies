# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 446
- HTTP: 123 alive / 81 gold
- HTTPS: 109 alive / 30 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47638
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
