# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 386
- HTTP: 106 alive / 62 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 190 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33088
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
