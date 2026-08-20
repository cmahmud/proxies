# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 384
- HTTP: 176 alive / 68 gold
- HTTPS: 138 alive / 20 gold
- SOCKS4: 194 alive / 142 gold
- SOCKS5: 217 alive / 154 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25562
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
