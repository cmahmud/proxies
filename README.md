# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 468
- HTTP: 132 alive / 96 gold
- HTTPS: 123 alive / 34 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 223 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46041
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
