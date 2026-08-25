# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 425
- HTTP: 96 alive / 67 gold
- HTTPS: 97 alive / 26 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35680
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
