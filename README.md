# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 412
- HTTP: 128 alive / 74 gold
- HTTPS: 181 alive / 18 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40398
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
