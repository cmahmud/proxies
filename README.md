# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 399
- HTTP: 121 alive / 73 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 186 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33268
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
