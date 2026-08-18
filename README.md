# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 239
- HTTP: 353 alive / 28 gold
- HTTPS: 135 alive / 9 gold
- SOCKS4: 247 alive / 115 gold
- SOCKS5: 231 alive / 87 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 321

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
