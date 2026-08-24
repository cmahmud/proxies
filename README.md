# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 392
- HTTP: 122 alive / 65 gold
- HTTPS: 54 alive / 9 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 189 alive / 161 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33323
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
