# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 427
- HTTP: 83 alive / 68 gold
- HTTPS: 72 alive / 27 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47147
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
