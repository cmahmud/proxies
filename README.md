# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 460
- HTTP: 133 alive / 87 gold
- HTTPS: 136 alive / 34 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46695
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
