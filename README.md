# SyndProxy private pool

## Current pool

- Alive now: 658
- Gold now: 385
- HTTP: 157 alive / 63 gold
- HTTPS: 96 alive / 20 gold
- SOCKS4: 203 alive / 151 gold
- SOCKS5: 202 alive / 151 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25727
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
