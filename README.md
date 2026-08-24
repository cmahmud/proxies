# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 398
- HTTP: 151 alive / 73 gold
- HTTPS: 69 alive / 15 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 192 alive / 154 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33268
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
