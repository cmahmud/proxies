# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 411
- HTTP: 133 alive / 72 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40438
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
