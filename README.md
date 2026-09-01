# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 473
- HTTP: 145 alive / 97 gold
- HTTPS: 123 alive / 36 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46343
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
