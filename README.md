# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 411
- HTTP: 143 alive / 74 gold
- HTTPS: 154 alive / 19 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 181 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40253
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
