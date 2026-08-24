# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 393
- HTTP: 90 alive / 54 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33491
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
