# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 475
- HTTP: 140 alive / 98 gold
- HTTPS: 130 alive / 38 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46946
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
