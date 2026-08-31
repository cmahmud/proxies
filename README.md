# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 494
- HTTP: 148 alive / 104 gold
- HTTPS: 143 alive / 51 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45006
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
