# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 384
- HTTP: 99 alive / 54 gold
- HTTPS: 33 alive / 11 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33459
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
