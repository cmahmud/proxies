# SyndProxy private pool

## Current pool

- Alive now: 1619
- Gold now: 628
- HTTP: 542 alive / 210 gold
- HTTPS: 470 alive / 117 gold
- SOCKS4: 232 alive / 144 gold
- SOCKS5: 375 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24060
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
