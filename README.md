# SyndProxy private pool

## Current pool

- Alive now: 861
- Gold now: 385
- HTTP: 272 alive / 79 gold
- HTTPS: 167 alive / 21 gold
- SOCKS4: 191 alive / 127 gold
- SOCKS5: 231 alive / 158 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29687
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
