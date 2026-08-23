# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 346
- HTTP: 116 alive / 40 gold
- HTTPS: 79 alive / 11 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 179 alive / 143 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32815
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
