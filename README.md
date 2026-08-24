# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 399
- HTTP: 160 alive / 73 gold
- HTTPS: 58 alive / 16 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 196 alive / 154 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33266
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
