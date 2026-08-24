# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 425
- HTTP: 154 alive / 75 gold
- HTTPS: 90 alive / 20 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 203 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33865
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
