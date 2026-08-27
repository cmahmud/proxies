# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 408
- HTTP: 115 alive / 65 gold
- HTTPS: 176 alive / 14 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41147
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
