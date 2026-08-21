# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 384
- HTTP: 265 alive / 76 gold
- HTTPS: 134 alive / 20 gold
- SOCKS4: 202 alive / 128 gold
- SOCKS5: 240 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29697
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
