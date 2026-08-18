# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 243
- HTTP: 232 alive / 29 gold
- HTTPS: 150 alive / 8 gold
- SOCKS4: 231 alive / 136 gold
- SOCKS5: 190 alive / 70 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9666
- Ever gold: 365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
