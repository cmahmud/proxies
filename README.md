# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 387
- HTTP: 79 alive / 52 gold
- HTTPS: 34 alive / 13 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 193 alive / 163 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33491
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
