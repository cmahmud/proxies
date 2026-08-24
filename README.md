# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 444
- HTTP: 129 alive / 86 gold
- HTTPS: 97 alive / 23 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34400
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
