# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 414
- HTTP: 129 alive / 71 gold
- HTTPS: 62 alive / 20 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 186 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33744
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
