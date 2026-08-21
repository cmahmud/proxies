# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 393
- HTTP: 241 alive / 87 gold
- HTTPS: 157 alive / 19 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 230 alive / 157 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27672
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
