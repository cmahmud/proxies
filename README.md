# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 402
- HTTP: 121 alive / 76 gold
- HTTPS: 57 alive / 15 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 192 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33273
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
